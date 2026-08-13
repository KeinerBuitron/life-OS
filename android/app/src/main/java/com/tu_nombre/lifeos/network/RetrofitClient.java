package com.tu_nombre.lifeos.network;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitClient {
    // 10.0.2.2 es el alias para localhost de tu PC desde el emulador de Android Studio.
    private static final String BASE_URL = "http://192.168.56.1/";
    private static Retrofit retrofit = null;

    public static ApiService getApiService() {
        if (retrofit == null) {
            retrofit = new Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();
        }
        return retrofit.create(ApiService.class);
    }
}