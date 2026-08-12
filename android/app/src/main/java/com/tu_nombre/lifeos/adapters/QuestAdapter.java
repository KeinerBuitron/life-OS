package com.tu_nombre.lifeos.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.tu_nombre.lifeos.R;
import com.tu_nombre.lifeos.models.QuestResponse;

import java.util.List;

public class QuestAdapter extends RecyclerView.Adapter<QuestAdapter.QuestViewHolder> {

    private List<QuestResponse> questList;
    private OnQuestClickListener listener;

    public interface OnQuestClickListener {
        void onCompleteClick(int questId);
    }

    public QuestAdapter(List<QuestResponse> questList, OnQuestClickListener listener) {
        this.questList = questList;
        this.listener = listener;
    }

    public void setQuests(List<QuestResponse> quests) {
        this.questList = quests;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public QuestViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_quest, parent, false);
        return new QuestViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull QuestViewHolder holder, int position) {
        QuestResponse quest = questList.get(position);
        holder.tvTitle.setText(quest.getTitle());
        holder.tvExp.setText("+" + quest.getExperience() + " EXP");

        if (quest.getState() == 1) {
            holder.btnComplete.setText("Completada");
            holder.btnComplete.setEnabled(false);
        } else {
            holder.btnComplete.setText("Completar");
            holder.btnComplete.setEnabled(true);
            holder.btnComplete.setOnClickListener(v -> listener.onCompleteClick(quest.getId()));
        }
    }

    @Override
    public int getItemCount() {
        return questList != null ? questList.size() : 0;
    }

    public static class QuestViewHolder extends RecyclerView.ViewHolder {
        TextView tvTitle, tvExp;
        Button btnComplete;

        public QuestViewHolder(@NonNull View itemView) {
            super(itemView);
            tvTitle = itemView.findViewById(R.id.tvQuestTitle);
            tvExp = itemView.findViewById(R.id.tvQuestExp);
            btnComplete = itemView.findViewById(R.id.btnComplete);
        }
    }
}