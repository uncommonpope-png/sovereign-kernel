const http = require('http');
const { LLMRouter } = require('./llm-router.js');
const PORT = parseInt(process.env.LLM_ROUTER_PORT || '3447', 10);

async function main() {
    const router = new LLMRouter();
    await router.autoSetup(process.cwd());

    const server = http.createServer(async (req, res) => {
        res.setHeader('Access-Control-Allow-Origin', '*');
        res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
        res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

        if (req.method === 'OPTIONS') {
            res.writeHead(204);
            res.end();
            return;
        }

        if (req.method !== 'POST' || req.url !== '/ask') {
            res.writeHead(404);
            res.end(JSON.stringify({ error: 'not found' }));
            return;
        }

        let body = '';
        req.on('data', c => body += c);
        req.on('end', async () => {
            try {
                const { systemPrompt, messages, maxTokens } = JSON.parse(body);
                const result = await router.ask(systemPrompt || '', messages || [{ role: 'user', content: '' }], maxTokens || 512);
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ success: true, response: result }));
            } catch (e) {
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ success: false, error: e.message }));
            }
        });
    });

    server.listen(PORT, '127.0.0.1', () => {
        console.log(`[LLMRouter-server] listening on 127.0.0.1:${PORT}`);
    });

    const health = http.createServer((req, res) => {
        res.writeHead(200);
        res.end(JSON.stringify({ status: 'alive', stats: router.stats }));
    });
    health.listen(PORT + 1, '0.0.0.0', () => {
        console.log(`[LLMRouter-health] on 0.0.0.0:${PORT + 1}`);
    });
}

main().catch(e => { console.error(e); process.exit(1); });
