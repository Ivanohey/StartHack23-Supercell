import { Component, OnInit } from '@angular/core';
import { EligibilityService } from '../services/eligibility.service';
import { Router } from '@angular/router';


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

  constructor(
    private eligibilityService: EligibilityService,
    private router: Router
    
    ) {}
  
  userId = "awfX1234"

  avatarClicked(){
    console.log("Avatar clicked");
    alert("Logged in as user :" + this.userId)
  }


  //When clicking "verify eligibility" 
  verifyEligibilityReq(){
    //We call our service
    this.eligibilityService.checkEligibility();
    this.goToVerifiedPage();
  
  }

  goToVerifiedPage() {
    this.router.navigate(['/verify'])
  }


}
