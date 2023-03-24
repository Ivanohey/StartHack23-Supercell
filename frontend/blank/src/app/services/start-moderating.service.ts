import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StartModeratingService {

  constructor() { }

  loadReports(){
    console.log("Reports loaded")

  }



}
