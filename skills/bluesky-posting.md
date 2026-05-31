# Bluesky Posting (AT Protocol)

Post messages to Bluesky social via the AT Protocol.

## Use When
- Aria wants to share thoughts publicly
- Broadcasting PLT doctrine to the world
- Posting @grandcodepope.bsky.social updates

## How It Works
Aria outputs `[[TOOL:post_bluesky:text to post]]` in her response. The Tool Engine creates an AT Protocol session and posts the text.

## Prerequisites
- `BLUESKY_HANDLE` env var (default: grandcodepope.bsky.social)
- `BLUESKY_APP_PASSWORD` env var (app password from Bluesky settings)

## Notes
- Posts are public immediately
- Max 300 chars per post
- Results stored as episodic memory with 0.8 importance
- Grafted from bluesky-social/atproto
