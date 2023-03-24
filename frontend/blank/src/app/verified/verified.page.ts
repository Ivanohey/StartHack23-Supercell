import { Component, OnInit } from '@angular/core';
import { StartModeratingService } from '../services/start-moderating.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-verified',
  templateUrl: './verified.page.html',
  styleUrls: ['./verified.page.scss']
})

export class VerifiedPage implements OnInit {
  checked = false;
  constructor(
    private startModeratingService: StartModeratingService,
    private router: Router
  ) { }

  ngOnInit() {
    
  }

  checkUncheck(checkedValue: any){
    if (!checkedValue){
      this.checked = true
    }
    else {
      this.checked = false;
    }
    console.log(this.checked);
  }

  startModerating(){
    
    this.startModeratingService.loadReports();
    this.router.navigate(["/moderation"]);
  }






}
