import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";
import { Project, Metric, Posture } from "@/types";

export const useProjects = () => {
  return useQuery({
    queryKey: ["projects"],
    queryFn: () => api.get<Project[]>("/projects"),
  });
};

export const useMetrics = () => {
  return useQuery({
    queryKey: ["metrics"],
    queryFn: () => api.get<Metric[]>("/metrics"),
  });
};

export const usePosture = () => {
  return useQuery({
    queryKey: ["posture"],
    queryFn: () => api.get<Posture[]>("/security/posture"),
  });
};
