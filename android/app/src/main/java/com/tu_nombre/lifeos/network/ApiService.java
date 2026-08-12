package com.tu_nombre.lifeos.network;

import com.tu_nombre.lifeos.models.CharacterResponse;
import com.tu_nombre.lifeos.models.QuestResponse;

import java.util.List;
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.PATCH;
import retrofit2.http.Path;

public interface ApiService {

    @GET("character/profile")
    Call<CharacterResponse> getProfile();

    @GET("quests")
    Call<List<QuestResponse>> getQuests();

    @PATCH("quests/{id}/complete")
    Call<QuestResponse> completeQuest(@Path("id") int id);
}