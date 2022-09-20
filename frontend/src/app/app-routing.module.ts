import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NetflixShowComponent } from './netflix-show/netflix-show.component';

const routes: Routes = [
  {path: 'netflix-shows', component: NetflixShowComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
