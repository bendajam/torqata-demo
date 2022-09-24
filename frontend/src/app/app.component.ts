import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <mat-grid-list cols="1" rowHeight="2:1">
      <app-header></app-header>
      <router-outlet></router-outlet>
      <app-footer></app-footer>
    </mat-grid-list>
  `, 
})
export class AppComponent { }