package de.mp.remote;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import java.net.URI;
import java.net.URISyntaxException;

import de.mp.remote.webocket.WebsocketClient;

public class MainActivity extends AppCompatActivity {

    public static WebsocketClient ws_client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}