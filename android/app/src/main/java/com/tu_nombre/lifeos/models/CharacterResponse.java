package com.tu_nombre.lifeos.models;

public class CharacterResponse {
    private int id;
    private String username;
    private int total_exp;
    private int current_streak;
    private int max_streak;
    private String last_completed_date;

    public int getId() { return id; }
    public String getUsername() { return username; }
    public int getTotalExp() { return total_exp; }
    public int getCurrentStreak() { return current_streak; }
    public int getMaxStreak() { return max_streak; }
    public String getLastCompletedDate() { return last_completed_date; }
}