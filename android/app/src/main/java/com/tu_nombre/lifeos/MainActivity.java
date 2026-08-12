package com.tu_nombre.lifeos;

import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.tu_nombre.lifeos.adapters.QuestAdapter;
import com.tu_nombre.lifeos.models.CharacterResponse;
import com.tu_nombre.lifeos.models.QuestResponse;
import com.tu_nombre.lifeos.network.RetrofitClient;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    private TextView tvUsername, tvTotalExp, tvCurrentStreak, tvMaxStreak;
    private RecyclerView rvQuests;
    private QuestAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvUsername = findViewById(R.id.tvUsername);
        tvTotalExp = findViewById(R.id.tvTotalExp);
        tvCurrentStreak = findViewById(R.id.tvCurrentStreak);
        tvMaxStreak = findViewById(R.id.tvMaxStreak);
        rvQuests = findViewById(R.id.rvQuests);

        rvQuests.setLayoutManager(new LinearLayoutManager(this));
        adapter = new QuestAdapter(new ArrayList<>(), this::completeQuest);
        rvQuests.setAdapter(adapter);

        loadProfileData();
        loadQuestsData();
    }

    private void loadProfileData() {
        RetrofitClient.getApiService().getProfile().enqueue(new Callback<CharacterResponse>() {
            @Override
            public void onResponse(Call<CharacterResponse> call, Response<CharacterResponse> response) {
                if (response.isSuccessful() && response.body() != null) {
                    CharacterResponse hero = response.body();
                    tvUsername.setText(hero.getUsername());
                    tvTotalExp.setText("EXP Total: " + hero.getTotalExp());
                    tvCurrentStreak.setText("🔥 Racha Actual: " + hero.getCurrentStreak() + " días");
                    tvMaxStreak.setText("🏆 Racha Máxima: " + hero.getMaxStreak() + " días");
                }
            }

            @Override
            public void onFailure(Call<CharacterResponse> call, Throwable t) {
                Toast.makeText(MainActivity.this, "Error al cargar perfil", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void loadQuestsData() {
        RetrofitClient.getApiService().getQuests().enqueue(new Callback<List<QuestResponse>>() {
            @Override
            public void onResponse(Call<List<QuestResponse>> call, Response<List<QuestResponse>> response) {
                if (response.isSuccessful() && response.body() != null) {
                    adapter.setQuests(response.body());
                }
            }

            @Override
            public void onFailure(Call<List<QuestResponse>> call, Throwable t) {
                Toast.makeText(MainActivity.this, "Error al cargar misiones", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void completeQuest(int questId) {
        RetrofitClient.getApiService().completeQuest(questId).enqueue(new Callback<QuestResponse>() {
            @Override
            public void onResponse(Call<QuestResponse> call, Response<QuestResponse> response) {
                if (response.isSuccessful()) {
                    Toast.makeText(MainActivity.this, "¡Misión completada!", Toast.LENGTH_SHORT).show();
                    loadProfileData();
                    loadQuestsData();
                }
            }

            @Override
            public void onFailure(Call<QuestResponse> call, Throwable t) {
                Toast.makeText(MainActivity.this, "No se pudo completar la misión", Toast.LENGTH_SHORT).show();
            }
        });
    }
}