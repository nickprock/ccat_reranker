from cat.mad_hatter.decorators import hook
from .rankers import get_settings, recent_ranker, litm, filter_ranker, sbert_ranker
from sentence_transformers import CrossEncoder

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
    # settings = get_settings()
    #TODO print(cat.working_memory.history[0]['message'])
    settings = cat.mad_hatter.get_plugin().load_settings()
    if settings["RECENTNESS"]:
        if cat.working_memory['episodic_memories']:
            recent_docs = recent_ranker(cat.working_memory['episodic_memories'])
            cat.working_memory['episodic_memories'] = recent_docs
        else:
            print("#HicSuntGattones")
    
    #TODO refactor
    if settings["SBERT"]:
        model = CrossEncoder(settings["ranker"])
        if cat.working_memory['declarative_memories']:
            sbert_docs = sbert_ranker(cat.working_memory['declarative_memories'], cat.working_memory.history[0]['message'], model)
            if settings["LITM"]:
                litm_docs = litm(sbert_docs)
                cat.working_memory['declarative_memories'] = litm_docs
            else:
                cat.working_memory['declarative_memories'] = sbert_docs
        else:
            print("#HicSuntGattones")
    else:
        if cat.working_memory['declarative_memories']:
            if settings["LITM"]:
                litm_docs = litm(cat.working_memory['declarative_memories'])
                cat.working_memory['declarative_memories'] = litm_docs
            else:
                print("#HicSuntGattones")
        else:
            print("#HicSuntGattones")
    
    if settings["FILTER"]:
        if cat.working_memory['procedural_memories']:
            filtered = filter_ranker(cat.working_memory['procedural_memories'], settings["tool_threshold"])
        else:
            print("#HicSuntGattones")
    pass # do nothing

