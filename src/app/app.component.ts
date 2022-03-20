import { Component, OnInit, ViewChild, Input } from "@angular/core";
import { Question, SimilarQuestion } from "./question";
import { QuestionService } from "./questionservice";
import { Table } from "primeng/table";
import { PrimeNGConfig, FilterService } from "primeng/api";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.scss"],
})

export class AppComponent implements OnInit {
  questions: Question[];

  loading: boolean = true;

  difficultyLevels = []

  topicTags = []

  @ViewChild("dt") table: Table;

  constructor(
    private questionService: QuestionService,
    private primengConfig: PrimeNGConfig,
    private filterService: FilterService
  ) {}

  ngOnInit() {
    this.questionService.getQuestions().then((questions) => {
      this.questions = questions;
      this.loading = false;

      for (const question of this.questions) {
        for (const tag of question.topicTags) {
          if (!this.topicTags.includes(tag)) {
            this.topicTags.push(tag)
          }
        }
      }
      this.topicTags.sort()
    });

    this.primengConfig.ripple = true;

    this.difficultyLevels = ['Easy', 'Medium', 'Hard'];

    this.initCustomFilter();
  }

  async initCustomFilter() {
    // register filter type for array items, when filter has one or more of values
    this.filterService.register("array-some", (value: any[], filters) => {
      if (filters === undefined || filters === null || filters.length === 0) {
          return true;
      }

      return filters.every(v => value.includes(v));
    });

    this.filterService.register("array-contain", (value: any[], filters) => {
      if (filters === undefined || filters === null || filters.length === 0) {
          return true;
      }

      return value.some(v => v.title.toLowerCase().indexOf(filters.toLowerCase()) != -1);
    });
  }


  onDifficultyLevelsChange(event) {
    this.table.filter(event.value, 'difficulty', 'in')
  }


  onTopicTagsChange(event) {
    this.table.filter(event.value, 'topicTags', 'array-some')
  }

  onSimilarQuestionsChange(event) {
    this.table.filter(event.value, 'similarQuestions', 'array-some')
  }

  onPaidOnlyChange(event) {
    this.table.filter(event.value, 'paidOnly', 'in')

    console.log(event.value)
  }
}
