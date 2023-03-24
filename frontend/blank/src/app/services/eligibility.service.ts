import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EligibilityService {

  constructor() { }

  checkEligibility(){
    console.log("I am eligibility service")
    

  }

}
