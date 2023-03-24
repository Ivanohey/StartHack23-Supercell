import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';

import {Routes, RouterModule } from '@angular/router'; 
import { HomePage } from './home/home.page';
import { VerifiedPage } from './verified/verified.page';
import { ModerationPage } from './moderation/moderation.page';


const appRoutes: Routes = [
  { path: '', component: HomePage },
  { path: '/verify', component: VerifiedPage},
  { path: '/moderation', component: ModerationPage}
]

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, IonicModule.forRoot(), AppRoutingModule],
  providers: [{ provide: RouteReuseStrategy, useClass: IonicRouteStrategy }],
  bootstrap: [AppComponent],
})


export class AppModule {}
