import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-task12',
  standalone: true,
  imports: [CommonModule ],
  templateUrl: './task12.component.html',
  styleUrl: './task12.component.css'
})
export class Task12Component {
  users = [
    { name: 'Dhanish Kumar', email: 'dhanish@gmail.com', contact: '1234567890' },
    { name: 'Hamsavanan', email: 'Hamsa@gmail.com', contact: '0987654321' },
    { name: 'Karupiya Saravanan', email: 'karupu@gmail.com', contact: '1122334455' },
  ];

}
