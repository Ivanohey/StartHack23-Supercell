import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})

export class HomePage implements OnInit {

  ngOnInit(): void {
    localStorage.setItem('userId', this.userId);
    console.log(localStorage.getItem('userId'))

    //Here we can implement the first request to fetch a random ID in the dataset





  }

  constructor() {}
  
  userId = "awfX1234"

  avatarClicked(){
    console.log("Avatar clicked");
    alert("Logged in as user :" + this.userId)
    
  }


}
