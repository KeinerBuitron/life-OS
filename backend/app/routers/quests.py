from fastapi import APIRouter
from app.schemas.quest import QuestCreate, QuestResponse
from fastapi import HTTPException  

router = APIRouter(prefix="/quests", tags=["Quests"])

quests_db = []

@router.post("/", response_model=QuestResponse)
def create_quest(quest: QuestCreate):
    
        new_id = len(quests_db) + 1
        new_quest = QuestResponse(
            id = new_id,
            state = False,
            date = "2024-06-01",
            title = quest.title,
            description = quest.description,
            experience = quest.experience,
    )
        quests_db.append(new_quest)
        return new_quest

@router.get("/", response_model=list[QuestResponse])
def get_quests():
    return quests_db

@router.patch("/{quest_id}", response_model=QuestResponse)
def update_quest(quest_id: int, quest: QuestCreate):
    for existing_quest in quests_db:
        if existing_quest.id == quest_id:
            existing_quest.title = quest.title
            existing_quest.description = quest.description
            existing_quest.experience = quest.experience
            return existing_quest
    raise HTTPException(status_code=404, detail="Quest not found")

@router.patch("/{quest_id}/complete", response_model=QuestResponse)
def complete_quest(quest_id: int):
    for existing_quest in quests_db:
        if existing_quest.id == quest_id:
            existing_quest.state = True
            return existing_quest
    raise HTTPException(status_code=404, detail="Quest not found")
