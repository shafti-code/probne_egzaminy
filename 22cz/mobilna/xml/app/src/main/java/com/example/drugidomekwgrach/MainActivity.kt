package com.example.drugidomekwgrach

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
        val likeButton = findViewById<Button>(R.id.likeB);
        val deleteButton = findViewById<Button>(R.id.deleteB);
        val saveButton = findViewById<Button>(R.id.saveB);
        val likes = findViewById<TextView>(R.id.likes);
        var likesCount = 0;
        likes.text = "$likesCount polubień";
        likeButton.setOnClickListener{
            likesCount++;
            likes.text = "$likesCount polubień";
        }

        deleteButton.setOnClickListener{
            likesCount--;
            likes.text = "$likesCount polubień";
        }
    }
}