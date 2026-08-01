from fastapi import APIRouter
from app.schemas.quest import QuestCreate, QuestResponse

router = APIRouter(prefix="/quests", tags=["Quests"])

@router.post("/", response_model=QuestResponse)
def create_quest(quest: QuestCreate):
    return QuestResponse(
        id = 1,
        state = False,
        date = "2026-08-02",
        title = quest.title,
        description = quest.description,
        experience = quest.experience
    )
