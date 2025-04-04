from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel


class MySettings(BaseModel):
    LITM: bool = False,
    RECENTNESS: bool = False,
    FILTER: bool = False,
    SBERT: bool = False
    ranker: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
    tool_threshold: float = 0.5

@plugin
def settings_schema():
    return MySettings.schema()
