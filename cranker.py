from cat.mad_hatter.decorators import hook
from .rankers import litm, get_settings, recentness


@hook(priority=1)
def after_cat_recalls_memories(cat) -> None:
    """Hook after semantic search in memories.

    The hook is executed just after the Cat searches for the meaningful context in memories
    and stores it in the *Working Memory*.

    Parameters
    ----------
    cat : CheshireCat
        Cheshire Cat instance.

    """
    settings = get_settings()
    if settings["RECENTNESS"]:
        if cat.working_memory['episodic_memories']:
            recent_docs = recentness(cat.working_memory['episodic_memories'])
            cat.working_memory['episodic_memories'] = recent_docs
        else:
            print("#HicSuntGattones")

    if settings["LITM"]:
        if cat.working_memory['declarative_memories']:
            litm_docs = litm(cat.working_memory['declarative_memories'])
            cat.working_memory['declarative_memories'] = litm_docs
        else:
            print("#HicSuntGattones")
    
    if settings["FILTER"]:
        if cat.working_memory['procedural_memories']:
            print("NON PUò ENTRAREEEEH!")
        else:
            print("#HicSuntGattones")
    pass # do nothing

