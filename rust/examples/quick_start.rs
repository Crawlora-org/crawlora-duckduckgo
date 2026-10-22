use crawlora_duckduckgo::{Client, DuckduckgoSearchParams, ModelDuckduckgoSearchResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .duckduckgo
        .search(DuckduckgoSearchParams {
            q: Some("open source web crawler".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelDuckduckgoSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
