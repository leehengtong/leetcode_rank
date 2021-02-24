import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Question } from "./question";

@Injectable()
export class QuestionService {
  constructor(private http: HttpClient) {}

  getQuestions() {
    return this.http
      .get<any>("assets/questions.json")
      .toPromise()
      .then((res) => <Question[]>res)
      .then((data) => {
        return data;
      });
  }
}
