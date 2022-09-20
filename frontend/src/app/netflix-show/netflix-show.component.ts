import {LiveAnnouncer} from '@angular/cdk/a11y';
import { Component, OnInit, ViewChild } from '@angular/core';
import { ShowService } from '../services/show.service';
import {MatPaginator, PageEvent} from '@angular/material/paginator';
import {MatSort, Sort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';

interface IResponse<T> {
  page: number,
  per_page: number,
  total: number,
  result: T[]
}

interface IShow {
  created_at: Date,
  date_added: Date,
  description: string,
  duration: number,
  id: number,
  rating: string,
  release_year: number,
  show_id: string,
  show_type: string,
  title: string,
  updated_at: Date,
}

@Component({
  selector: 'app-netflix-show',
  templateUrl: './netflix-show.component.html',
  styleUrls: ['./netflix-show.component.scss']
})
export class NetflixShowComponent implements OnInit {
  displayedColumns: string[] = ['title', 'description'];
  dataSource = new MatTableDataSource<IShow>;
  total: number;
  sortState: Sort;
  pageState: PageEvent;

  @ViewChild(MatPaginator) paginator: MatPaginator;  
  @ViewChild(MatSort) sort: MatSort; 

  constructor(private _liveAnnouncer: LiveAnnouncer, private service:ShowService) {
  }

  getShows(page?: number, perPage?: number, sortItem?: string, sortDir?: string) {
    this.service.getShows(page, perPage, sortItem, sortDir)
      .subscribe((response: IResponse<IShow>) => {
        this.dataSource.data = response.result;
        this.total = response.total;
      });
  }

  ngOnInit(): void {
    this.getShows()
    this.dataSource.paginator = this.paginator;
  }

  /** Announce the change in sort state for assistive technology. */
  announceSortChange(sortState: Sort) {
    this.sortState = sortState;
    this.filterShows();
    // This example uses English messages. If your application supports
    // multiple language, you would internationalize these strings.
    // Furthermore, you can customize the message to add additional
    // details about the values being sorted.
    if (sortState.direction) {
      this._liveAnnouncer.announce(`Sorted ${sortState.direction}ending`);
    } else {
      this._liveAnnouncer.announce('Sorting cleared');
    }
  }
  changePage( pageEvent: PageEvent) {
    this.pageState = pageEvent;
    this.filterShows();
  }

  filterShows(){
    this.getShows(this.pageState?.pageIndex, this.pageState?.pageSize, this.sortState?.active, this.sortState?.direction);

  }
}
