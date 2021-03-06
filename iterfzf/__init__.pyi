from typing import Dict, AnyStr, Iterable, Optional

BUNDLED_EXECUTABLE: Optional[str]

def iterfzf(
    iterable: Iterable[AnyStr], *,
    # Search mode:
    extended: bool = ...,
    exact: bool = ...,
    case_sensitive: Optional[bool] = ...,
    # Interface:
    multi: bool = ...,
    mouse: bool = ...,
    print_query: bool = ...,
    header: Optional[str] = ...,
    color: Optional[Dict[str,str]] = ...,
    # Layout:
    prompt: str = ...,
    preview: Optional[str] = ...,
    # Misc:
    query: str = ...,
    encoding: Optional[str] = ...,
    executable: str = ...,
) -> Iterable[AnyStr]: ...
