import { Component, OnInit, ViewChild, Input } from "@angular/core";
import { Question, SimilarQuestion } from "./question";
import { QuestionService } from "./questionservice";
import { Table } from "primeng/table";
import { PrimeNGConfig } from "primeng/api";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.scss"],
})

export class AppComponent implements OnInit {
  questions: Question[];

  loading: boolean = true;

  @ViewChild("dt") table: Table;

  constructor(
    private questionService: QuestionService,
    private primengConfig: PrimeNGConfig
  ) {}

  ngOnInit() {
    this.questionService.getQuestions().then((questions) => {
      this.questions = questions;
      this.loading = false;
    });

    this.primengConfig.ripple = true;
  }
}
