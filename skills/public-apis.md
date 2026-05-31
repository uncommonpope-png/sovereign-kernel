# public-apis — Free API Gateway

Grafted from public-apis/public-apis (437k+ stars on GitHub).

Aria can call any REST API from the public-apis directory. Supports GET, POST, PUT, DELETE.

## Usage
```rust
skill_call_api("GET", "https://api.example.com/data", None, None).await
skill_call_api("POST", "https://api.example.com/data", Some("token"), Some(r#"{"key":"value"}"#)).await
```

Returns HTTP status and response body (truncated to 2000 chars).
