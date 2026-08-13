package com.tu_nombre.lifeos.models;

import com.google.gson.annotations.SerializedName;

public class QuestResponse {
    private int id;
    private String title;
    private String description;
    private int experience;
    private boolean state;
    private String date;

    // --- GETTERS Y SETTERS ---
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public int getExperience() { return experience; }
    public void setExperience(int experience) { this.experience = experience; }

    public boolean isState() { return state; }
    public void setState(boolean state) { this.state = state; }

    public String getDate() { return date; }
    public void setDate(String date) { this.date = date; }
}