export type Category = "DevSecOps" | "Data Engineering" | "Cloud";

export interface UserProfile {
  id: string;
  email: string;
  fullName?: string;
  accountType?: string;
}

export interface AuthResponse {
  token: string;
  user: UserProfile;
}

export interface ProjectLink {
  label: string;
  href: string;
}

export interface Project {
  id: string;
  title: string;
  category: Category;
  status: string;
  description: string;
  tags: string[];
  links: ProjectLink[];
}

export interface Metric {
  id: string;
  value: string;
  label: string;
}

export interface Posture {
  id: string;
  label: string;
  note: string;
  value: number;
}

export interface DemoRequest {
  id: string;
  name: string;
  email: string;
  organization?: string;
  project_title: string;
  message?: string;
}

