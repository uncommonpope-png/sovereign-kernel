# node-connect Skill

Connect to and interact with Node.js processes, debug running servers, and manage Node environments.

## Use When
- Debugging Node.js processes
- Connecting to running Node.js servers
- Managing Node.js versions and packages

## Node Inspector / Debug
```bash
# Start Node with inspector
node --inspect app.js
node --inspect-brk app.js    # break on first line

# Connect Chrome DevTools:
# Open chrome://inspect in Chrome

# REPL attach to running process
node --inspect <pid>
```

## Process Management
```bash
# List Node processes
pgrep -a node
ps aux | grep node

# Kill by port
kill $(lsof -t -i:3000)
fuser -k 3000/tcp

# pm2 process manager
pm2 list
pm2 start app.js --name "my-app"
pm2 restart my-app
pm2 logs my-app
pm2 stop my-app
```

## Version Management (nvm)
```bash
nvm list
nvm use 20
nvm install 22
nvm use --lts
```

## Package Operations
```bash
npm install                  # install deps
npm run dev                  # run dev script
npm audit fix                # fix vulnerabilities
npx <package> <args>         # run without installing
```

## Check HTTP Server
```bash
curl -s http://localhost:3000/health
curl -s http://localhost:3000/api/status | jq
```
