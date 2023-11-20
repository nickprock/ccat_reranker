from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field


class MySettings(BaseModel):
    LITM: bool = True,
    RECENTNESS: bool = True,
    FILTER: bool = True,
    tool_threshold: float = 0.5

@plugin
def settings_schema():
    return MySettings.schema()