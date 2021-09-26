package com.example.myapplication;

import android.Manifest;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        requestPermissions(new String[]{Manifest.permission.ACCESS_WIFI_STATE,Manifest.permission.READ_PHONE_STATE,Manifest.permission.INTERNET,Manifest.permission.ACCESS_NETWORK_STATE,Manifest.permission.READ_EXTERNAL_STORAGE,Manifest.permission.CAMERA,Manifest.permission.RECORD_AUDIO,Manifest.permission.WRITE_EXTERNAL_STORAGE},100);

        View login = findViewById(R.id.login);
        login.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                Intent intent=new Intent(MainActivity.this, LoginActivity.class);
                startActivity(intent);

            }
        });

        View registration=findViewById(R.id.registration);
        registration.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                Intent intent=new Intent(MainActivity.this,RegistrationActivity.class);
                startActivity(intent);
            }
        });
    }
}