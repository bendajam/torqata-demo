import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NetflixShowComponent } from './netflix-show.component';

describe('NetflixShowComponent', () => {
  let component: NetflixShowComponent;
  let fixture: ComponentFixture<NetflixShowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NetflixShowComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NetflixShowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
