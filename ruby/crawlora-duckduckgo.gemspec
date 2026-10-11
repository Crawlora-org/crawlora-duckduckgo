require_relative "lib/crawlora/duckduckgo/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-duckduckgo"
  spec.version = Crawlora::Duckduckgo::VERSION
  spec.summary = "DuckDuckGo API client for Crawlora (6 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted DuckDuckGo API. Covers web, news, image, video, and shopping search plus query suggestions across 6 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-duckduckgo", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
