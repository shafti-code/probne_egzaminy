package com.example.domwgorach

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.domwgorach.ui.theme.DomWGorachTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            DomWGorachTheme {
                HomeScreen()
            }
        }
    }
}

@Composable
fun HomeScreen() {
    var likes by remember { mutableStateOf(0) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("Domek w górach", fontSize = 24.sp, fontWeight = FontWeight.Bold)
        Spacer(Modifier.height(8.dp))

        Image(
            painter = painterResource(R.drawable.house),
            contentDescription = "house image",
            modifier = Modifier
                .fillMaxWidth()
                .height(200.dp)
        )

        Spacer(Modifier.height(8.dp))

        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceEvenly
        ) {
            Button(onClick = { likes++ }) { Text("Like") }
            Button(onClick = { /* save */ }) { Text("Save") }
            Button(onClick = { likes-- }) { Text("Delete") }
        }

        Spacer(Modifier.height(8.dp))
        Text("Likes: $likes")
        Divider(Modifier.padding(vertical = 8.dp))
        Text("Opis domku w górach…", modifier = Modifier.fillMaxWidth())
    }
}

