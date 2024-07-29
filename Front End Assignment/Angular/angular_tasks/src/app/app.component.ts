import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule} from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Task11Component } from './component/task11/task11.component';
import { Task12Component } from './component/task12/task12.component'; 
import { Task13Component } from './component/task13/task13.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,FormsModule,CommonModule,Task11Component,Task12Component,Task13Component],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'angular_tasks';
}
