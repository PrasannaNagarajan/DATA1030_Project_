try:
    from ipumspy import IpumsApiClient  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - optional dependency for local development
    IpumsApiClient = None

API_KEY = '59cba10d8a5da536fc06b59db6fbb6b155db435d9b1cf4c4ffd59d42'

if IpumsApiClient is not None:
    ipums = IpumsApiClient(API_KEY)
else:
    ipums = None

__all__ = ["ipums"]
