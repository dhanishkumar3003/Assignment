import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Task12Component } from './task12.component';

describe('Task12Component', () => {
  let component: Task12Component;
  let fixture: ComponentFixture<Task12Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Task12Component]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Task12Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
