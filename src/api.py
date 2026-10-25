import os

from dotenv import load_dotenv

try:
    from ipumspy import IpumsApiClient  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - optional dependency for local development
    IpumsApiClient = None

# Load the API key from a local .env file (the .env file is gitignored, never commit it).
# Create a .env file in the project root containing:  IPUMS_API_KEY=your_key_here
load_dotenv()
API_KEY = os.environ.get("IPUMS_API_KEY")

if IpumsApiClient is not None and API_KEY:
    ipums = IpumsApiClient(API_KEY)
else:
    ipums = None

__all__ = ["ipums"]
