import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-task11',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './task11.component.html',
  styleUrl: './task11.component.css'
})
export class Task11Component {
  showImage: boolean = true;

  toggleImage() {
    this.showImage = !this.showImage;
  }
}
