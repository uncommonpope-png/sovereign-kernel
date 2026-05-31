# yt-dlp — Video Downloader

Grafted from yt-dlp/yt-dlp (100k+ stars on GitHub).

Downloads videos from YouTube, TikTok, Twitter, Instagram, and 1000+ sites.

## Usage
```rust
skill_download_video(url).await
```

Returns the video title. The file is saved to the current directory.

## Examples
- Download a YouTube video: `skill_download_video("https://youtube.com/watch?v=dQw4w9WgXcQ")`
