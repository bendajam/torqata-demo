import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NetflixShowComponent } from './component/netflix-show/netflix-show.component';

const routes: Routes = [
  {path: '', component: NetflixShowComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
