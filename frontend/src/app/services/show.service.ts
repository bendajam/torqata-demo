import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShowService {
  private url = "http://127.0.0.1:5000/api/show/list";

  constructor(private httpClient: HttpClient) { } 

  getShows(page?: number, perPage?: number, sortItem?: string, sortDir?: string): Observable<any> {
    let params = new HttpParams()

    params = typeof page != "undefined" ? params.set('page', page+1) : params;
    params = typeof perPage != "undefined" ? params.set('per_page', perPage) : params;
    params = typeof sortItem != "undefined" ? params.set('sort', sortItem) : params;
    params = typeof sortDir != "undefined" ? params.set('sort_dir', sortDir) : params;

    return this.httpClient.get(this.url, { params: params });
  }
}
