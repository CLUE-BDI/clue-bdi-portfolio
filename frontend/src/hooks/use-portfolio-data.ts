import { useQuery } from "@tanstack/react-query";
import { apiClient } from "../lib/api-client";
import { Project, Metric, Posture } from "../types/api";

export const useProjects = () => {
  return useQuery({
    queryKey: ["projects"],
    queryFn: () => apiClient.get<Project[]>("/projects"),
  });
};

export const useMetrics = () => {
  return useQuery({
    queryKey: ["metrics"],
    queryFn: () => apiClient.get<Metric[]>("/metrics"),
  });
};

export const usePosture = () => {
  return useQuery({
    queryKey: ["posture"],
    queryFn: () => apiClient.get<Posture[]>("/security/posture"),
  });
};
