export interface SimilarQuestion {
  title?: string;
  titleSlug?: string;
}

export interface Question {
  questionId?: number;
  questionFrontendId?: number;
  boundTopicId?: string;
  title?: string;
  titleSlug?: string;
  isPaidOnly?: true;
  difficulty?: string;
  likes?: number;
  dislikes?: number;
  isLiked?: boolean;
  similarQuestions?: SimilarQuestion[];
  contributors?: string[];
  topicTags?: string[];
  link?: string;
  questionHide?: boolean;
  totalAc?: number;
  totalSubmit?: number;
  isNewQuestion?: boolean;
  paidOnly?: boolean;
}
