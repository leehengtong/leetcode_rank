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
  question__hide?: boolean;
  total_acs?: number;
  total_submitted?: number;
  is_new_question?: boolean;
  paid_only?: boolean;
}
