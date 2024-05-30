from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field


class MySettings(BaseModel):
    LITM: bool = True,
    RECENTNESS: bool = True,
    FILTER: bool = True,
    SBERT: bool = True
    ranker: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
    tool_threshold: float = 0.5

@plugin
def settings_schema():
    return MySettings.schema()