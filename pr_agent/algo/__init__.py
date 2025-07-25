MAX_TOKENS = {
    'text-embedding-ada-002': 8000,
    'gpt-3.5-turbo': 16000,
    'gpt-3.5-turbo-0125': 16000,
    'gpt-3.5-turbo-0613': 4000,
    'gpt-3.5-turbo-1106': 16000,
    'gpt-3.5-turbo-16k': 16000,
    'gpt-3.5-turbo-16k-0613': 16000,
    'gpt-4': 8000,
    'gpt-4-0613': 8000,
    'gpt-4-32k': 32000,
    'gpt-4-1106-preview': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4-0125-preview': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4o': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4o-2024-05-13': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4-turbo-preview': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4-turbo-2024-04-09': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4-turbo': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4o-mini': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4o-mini-2024-07-18': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4o-2024-08-06': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4o-2024-11-20': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4.5-preview': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4.5-preview-2025-02-27': 128000,  # 128K, but may be limited by config.max_model_tokens
    'gpt-4.1': 1047576,
    'gpt-4.1-2025-04-14': 1047576,
    'gpt-4.1-mini': 1047576,
    'gpt-4.1-mini-2025-04-14': 1047576,
    'gpt-4.1-nano': 1047576,
    'gpt-4.1-nano-2025-04-14': 1047576,
    'o1-mini': 128000,  # 128K, but may be limited by config.max_model_tokens
    'o1-mini-2024-09-12': 128000,  # 128K, but may be limited by config.max_model_tokens
    'o1-preview': 128000,  # 128K, but may be limited by config.max_model_tokens
    'o1-preview-2024-09-12': 128000,  # 128K, but may be limited by config.max_model_tokens
    'o1-2024-12-17': 204800,  # 200K, but may be limited by config.max_model_tokens
    'o1': 204800,  # 200K, but may be limited by config.max_model_tokens
    'o3-mini': 204800,  # 200K, but may be limited by config.max_model_tokens
    'o3-mini-2025-01-31': 204800,  # 200K, but may be limited by config.max_model_tokens
    'o3': 200000,  # 200K, but may be limited by config.max_model_tokens
    'o3-2025-04-16': 200000,  # 200K, but may be limited by config.max_model_tokens
    'o4-mini': 200000, # 200K, but may be limited by config.max_model_tokens
    'o4-mini-2025-04-16': 200000, # 200K, but may be limited by config.max_model_tokens
    'claude-instant-1': 100000,
    'claude-2': 100000,
    'command-nightly': 4096,
    'deepseek/deepseek-chat': 128000,  # 128K, but may be limited by config.max_model_tokens
    'deepseek/deepseek-reasoner': 64000,  # 64K, but may be limited by config.max_model_tokens
    'openai/qwq-plus': 131072,  # 131K context length, but may be limited by config.max_model_tokens
    'replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1': 4096,
    'meta-llama/Llama-2-7b-chat-hf': 4096,
    'vertex_ai/codechat-bison': 6144,
    'vertex_ai/codechat-bison-32k': 32000,
    'vertex_ai/claude-3-haiku@20240307': 100000,
    'vertex_ai/claude-3-5-haiku@20241022': 100000,
    'vertex_ai/claude-3-sonnet@20240229': 100000,
    'vertex_ai/claude-3-opus@20240229': 100000,
    'vertex_ai/claude-opus-4@20250514': 200000,
    'vertex_ai/claude-3-5-sonnet@20240620': 100000,
    'vertex_ai/claude-3-5-sonnet-v2@20241022': 100000,
    'vertex_ai/claude-3-7-sonnet@20250219': 200000,
    'vertex_ai/claude-sonnet-4@20250514': 200000,
    'vertex_ai/gemini-1.5-pro': 1048576,
    'vertex_ai/gemini-2.5-pro-preview-03-25': 1048576,
    'vertex_ai/gemini-2.5-pro-preview-05-06': 1048576,
    'vertex_ai/gemini-2.5-pro-preview-06-05': 1048576,
    'vertex_ai/gemini-2.5-pro': 1048576,
    'vertex_ai/gemini-1.5-flash': 1048576,
    'vertex_ai/gemini-2.0-flash': 1048576,
    'vertex_ai/gemini-2.5-flash-preview-04-17': 1048576,
    'vertex_ai/gemini-2.5-flash-preview-05-20': 1048576,
    'vertex_ai/gemini-2.5-flash': 1048576,
    'vertex_ai/gemma2': 8200,
    'gemini/gemini-1.5-pro': 1048576,
    'gemini/gemini-1.5-flash': 1048576,
    'gemini/gemini-2.0-flash': 1048576,
    'gemini/gemini-2.5-flash-preview-04-17': 1048576,
    'gemini/gemini-2.5-flash-preview-05-20': 1048576,
    'gemini/gemini-2.5-flash': 1048576,
    'gemini/gemini-2.5-pro-preview-03-25': 1048576,
    'gemini/gemini-2.5-pro-preview-05-06': 1048576,
    'gemini/gemini-2.5-pro-preview-06-05': 1048576,
    'gemini/gemini-2.5-pro': 1048576,
    'codechat-bison': 6144,
    'codechat-bison-32k': 32000,
    'anthropic.claude-instant-v1': 100000,
    'anthropic.claude-v1': 100000,
    'anthropic.claude-v2': 100000,
    'anthropic/claude-3-opus-20240229': 100000,
    'anthropic/claude-opus-4-20250514': 200000,
    'anthropic/claude-3-5-sonnet-20240620': 100000,
    'anthropic/claude-3-5-sonnet-20241022': 100000,
    'anthropic/claude-3-7-sonnet-20250219': 200000,
    'anthropic/claude-sonnet-4-20250514': 200000,
    'claude-3-7-sonnet-20250219': 200000,
    'anthropic/claude-3-5-haiku-20241022': 100000,
    'bedrock/anthropic.claude-instant-v1': 100000,
    'bedrock/anthropic.claude-v2': 100000,
    'bedrock/anthropic.claude-v2:1': 100000,
    'bedrock/anthropic.claude-3-sonnet-20240229-v1:0': 100000,
    'bedrock/anthropic.claude-opus-4-20250514-v1:0': 200000,
    'bedrock/anthropic.claude-3-haiku-20240307-v1:0': 100000,
    'bedrock/anthropic.claude-3-5-haiku-20241022-v1:0': 100000,
    'bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0': 100000,
    'bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0': 100000,
    'bedrock/anthropic.claude-3-7-sonnet-20250219-v1:0': 200000,
    'bedrock/anthropic.claude-sonnet-4-20250514-v1:0': 200000,
    "bedrock/us.anthropic.claude-opus-4-20250514-v1:0": 200000,
    "bedrock/us.anthropic.claude-3-5-sonnet-20241022-v2:0": 100000,
    "bedrock/us.anthropic.claude-3-7-sonnet-20250219-v1:0": 200000,
    "bedrock/us.anthropic.claude-sonnet-4-20250514-v1:0": 200000,
    "bedrock/apac.anthropic.claude-3-5-sonnet-20241022-v2:0": 100000,
    "bedrock/apac.anthropic.claude-3-7-sonnet-20250219-v1:0": 200000,
    "bedrock/apac.anthropic.claude-sonnet-4-20250514-v1:0": 200000,
    'claude-3-5-sonnet': 100000,
    'groq/meta-llama/llama-4-scout-17b-16e-instruct': 131072,
    'groq/meta-llama/llama-4-maverick-17b-128e-instruct': 131072,
    'bedrock/us.meta.llama4-scout-17b-instruct-v1:0': 128000,
    'bedrock/us.meta.llama4-maverick-17b-instruct-v1:0': 128000,
    'groq/llama3-8b-8192': 8192,
    'groq/llama3-70b-8192': 8192,
    'groq/llama-3.1-8b-instant': 8192,
    'groq/llama-3.3-70b-versatile': 128000,
    'groq/mixtral-8x7b-32768': 32768,
    'groq/gemma2-9b-it': 8192,
    'xai/grok-2': 131072,
    'xai/grok-2-1212': 131072,
    'xai/grok-2-latest': 131072,
    'xai/grok-3': 131072,
    'xai/grok-3-beta': 131072,
    'xai/grok-3-fast': 131072,
    'xai/grok-3-fast-beta': 131072,
    'xai/grok-3-mini': 131072,
    'xai/grok-3-mini-beta': 131072,
    'xai/grok-3-mini-fast': 131072,
    'xai/grok-3-mini-fast-beta': 131072,
    'ollama/llama3': 4096,
    'watsonx/meta-llama/llama-3-8b-instruct': 4096,
    "watsonx/meta-llama/llama-3-70b-instruct": 4096,
    "watsonx/meta-llama/llama-3-405b-instruct": 16384,
    "watsonx/ibm/granite-13b-chat-v2": 8191,
    "watsonx/ibm/granite-34b-code-instruct": 8191,
    "watsonx/mistralai/mistral-large": 32768,
    "deepinfra/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B": 128000,
    "deepinfra/deepseek-ai/DeepSeek-R1-Distill-Llama-70B": 128000,
    "deepinfra/deepseek-ai/DeepSeek-R1": 128000,
    "mistral/mistral-small-latest": 8191,
    "mistral/mistral-medium-latest": 8191,
    "mistral/mistral-large-2407": 128000,
    "mistral/mistral-large-latest": 128000,
    "mistral/open-mistral-7b": 8191,
    "mistral/open-mixtral-8x7b": 8191,
    "mistral/open-mixtral-8x22b": 8191,
    "mistral/codestral-latest": 8191,
    "mistral/open-mistral-nemo": 128000,
    "mistral/open-mistral-nemo-2407": 128000,
    "mistral/open-codestral-mamba": 256000,
    "mistral/codestral-mamba-latest": 256000,
    "codestral/codestral-latest": 8191,
    "codestral/codestral-2405": 8191,
}

USER_MESSAGE_ONLY_MODELS = [
    "deepseek/deepseek-reasoner",
    "o1-mini",
    "o1-mini-2024-09-12",
    "o1-preview"
]

NO_SUPPORT_TEMPERATURE_MODELS = [
    "deepseek/deepseek-reasoner",
    "o1-mini",
    "o1-mini-2024-09-12",
    "o1",
    "o1-2024-12-17",
    "o3-mini",
    "o3-mini-2025-01-31",
    "o1-preview",
    "o3",
    "o3-2025-04-16",
    "o4-mini",
    "o4-mini-2025-04-16",
]

SUPPORT_REASONING_EFFORT_MODELS = [
    "o3-mini",
    "o3-mini-2025-01-31",
    "o3",
    "o3-2025-04-16",
    "o4-mini",
    "o4-mini-2025-04-16",
]

CLAUDE_EXTENDED_THINKING_MODELS = [
    "anthropic/claude-3-7-sonnet-20250219",
    "claude-3-7-sonnet-20250219"
]

# Models that require streaming mode
STREAMING_REQUIRED_MODELS = [
    "openai/qwq-plus"
]
