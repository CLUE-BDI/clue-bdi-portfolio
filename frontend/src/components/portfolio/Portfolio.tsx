import { FormEvent, ReactNode, useEffect, useMemo, useState } from "react";
import { useAuth } from "@/contexts/AuthContext";
import { useProjects, useMetrics, usePosture } from "@/hooks/usePortfolio";
import { Project, Metric, Posture, Category } from "@/types";
import { Link } from "react-router-dom";

/* ---------------- Data ---------------- */

const NAV_ITEMS = [
  { label: "Home", href: "#home" },
  { label: "Projects", href: "#projects" },
  { label: "Demos", href: "#demos" },
  { label: "Architecture", href: "#architecture" },
  { label: "Contact", href: "#contact" },
];

const SKILLS = ["AWS", "Kubernetes", "Terraform", "GitLab CI", "Python", "BigQuery"];

const CATEGORIES = ["All", "DevSecOps", "Data Engineering", "Cloud"] as const;

const ARCH_STEPS = [
  { title: "Commit", text: "Developer pushes code" },
  { title: "CI/CD", text: "Scan, build, deploy" },
  { title: "Security", text: "Normalize findings" },
  { title: "Cloud", text: "Blue/green release" },
  { title: "Warehouse", text: "Store analytics" },
  { title: "Dashboard", text: "Show impact" },
];

const TABLE_ROWS = [
  ["Project cards", "Title, summary, stack tags, buttons", "Fast recruiter scanning"],
  ["Tabs / filters", "All, DevSecOps, Data Engineering, Cloud", "Organize portfolio areas"],
  ["Tech stack table", "Layer, tool, role", "Show engineering depth"],
  ["Demo links", "Live demo, repo, dashboard", "Prove hands-on capability"],
  ["Metrics", "Before vs after results", "Show business/security impact"],
];

const DEMO_CHECKLIST = [
  "Blue: intentionally vulnerable demo app",
  "Security scan: findings collected in CI/CD",
  "Green: patched deployment released safely",
  "Dashboard: vulnerability count reduced",
];

const ACCOUNT_TYPES = [
  "Recruiter / Hiring Manager",
  "Collaborator",
  "Student / Learner",
  "Client / Partner",
];

/* ---------------- Validation ---------------- */
/* Data validation removed as data is now dynamic */

/* ---------------- Icons (inline SVG) ---------------- */

const Icon = ({ name, className = "h-4 w-4" }: { name: string; className?: string }) => {
  const props = {
    className,
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 2,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
    viewBox: "0 0 24 24",
  };
  switch (name) {
    case "shield":
      return (
        <svg {...props}>
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
        </svg>
      );
    case "download":
      return (
        <svg {...props}>
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
          <polyline points="7 10 12 15 17 10" />
          <line x1="12" y1="15" x2="12" y2="3" />
        </svg>
      );
    case "arrow":
      return (
        <svg {...props}>
          <line x1="5" y1="12" x2="19" y2="12" />
          <polyline points="12 5 19 12 12 19" />
        </svg>
      );
    case "play":
      return (
        <svg {...props}>
          <polygon points="6 3 20 12 6 21 6 3" />
        </svg>
      );
    case "check":
      return (
        <svg {...props}>
          <polyline points="20 6 9 17 4 12" />
        </svg>
      );
    case "close":
      return (
        <svg {...props}>
          <line x1="18" y1="6" x2="6" y2="18" />
          <line x1="6" y1="6" x2="18" y2="18" />
        </svg>
      );
    case "menu":
      return (
        <svg {...props}>
          <line x1="3" y1="6" x2="21" y2="6" />
          <line x1="3" y1="12" x2="21" y2="12" />
          <line x1="3" y1="18" x2="21" y2="18" />
        </svg>
      );
    case "github":
      return (
        <svg {...props}>
          <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" />
        </svg>
      );
    case "linkedin":
      return (
        <svg {...props}>
          <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z" />
          <rect x="2" y="9" width="4" height="12" />
          <circle cx="4" cy="4" r="2" />
        </svg>
      );
    case "mail":
      return (
        <svg {...props}>
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
          <polyline points="22,6 12,13 2,6" />
        </svg>
      );
    default:
      return null;
  }
};

/* ---------------- Reusable bits ---------------- */

const Pill = ({ children }: { children: ReactNode }) => (
  <span className="inline-flex items-center rounded-full border border-border bg-secondary/40 px-3 py-1 text-xs font-medium text-muted-foreground">
    {children}
  </span>
);

const SectionHeading = ({
  eyebrow,
  title,
  subtitle,
  center = false,
}: {
  eyebrow?: string;
  title: string;
  subtitle?: string;
  center?: boolean;
}) => (
  <div className={`mb-12 ${center ? "text-center mx-auto max-w-2xl" : "max-w-3xl"}`}>
    {eyebrow && (
      <div className="mb-3 text-xs font-semibold uppercase tracking-widest text-primary">
        {eyebrow}
      </div>
    )}
    <h2 className="text-3xl font-bold tracking-tight sm:text-4xl">{title}</h2>
    {subtitle && <p className="mt-4 text-muted-foreground">{subtitle}</p>}
  </div>
);

const Button = ({
  children,
  variant = "primary",
  size = "md",
  onClick,
  type = "button",
  className = "",
}: {
  children: ReactNode;
  variant?: "primary" | "secondary" | "ghost" | "outline";
  size?: "sm" | "md" | "lg";
  onClick?: () => void;
  type?: "button" | "submit";
  className?: string;
}) => {
  const sizes = {
    sm: "px-3 py-1.5 text-sm",
    md: "px-4 py-2 text-sm",
    lg: "px-6 py-3 text-base",
  };
  const variants = {
    primary:
      "bg-primary-gradient text-primary-foreground font-semibold shadow-glow hover:opacity-90",
    secondary:
      "bg-secondary text-foreground border border-border hover:bg-secondary/70",
    ghost: "text-muted-foreground hover:text-foreground",
    outline:
      "border border-primary/40 text-primary hover:bg-primary/10",
  };
  return (
    <button
      type={type}
      onClick={onClick}
      className={`inline-flex items-center justify-center gap-2 rounded-lg transition ${sizes[size]} ${variants[variant]} ${className}`}
    >
      {children}
    </button>
  );
};

/* ---------------- Project Card ---------------- */

const ProjectCard = ({ project }: { project: Project }) => (
  <div className="group flex flex-col rounded-2xl border border-border bg-card/60 p-6 shadow-card backdrop-blur transition hover:border-primary/40 hover:shadow-glow">
    <div className="mb-4 flex items-center justify-between">
      <span className="text-xs font-semibold uppercase tracking-wider text-primary">
        {project.category}
      </span>
      <span className="rounded-full border border-primary/30 bg-primary/10 px-2.5 py-0.5 text-xs font-medium text-primary">
        {project.status}
      </span>
    </div>
    <h3 className="text-xl font-semibold">{project.title}</h3>
    <p className="mt-2 flex-1 text-sm text-muted-foreground">{project.description}</p>
    <div className="mt-4 flex flex-wrap gap-2">
      {project.tags.map((t) => (
        <Pill key={t}>{t}</Pill>
      ))}
    </div>
    <div className="mt-6 flex flex-wrap gap-2">
      {project.links.map((l, i) => (
        <Button 
          key={l.label} 
          variant={i === 0 ? "outline" : "ghost"} 
          size="sm"
          onClick={() => {
            if (l.href && l.href !== "#") window.open(l.href, "_blank");
          }}
        >
          {l.label}
          <Icon name="arrow" className="h-3.5 w-3.5" />
        </Button>
      ))}
    </div>
  </div>
);

/* ---------------- Auth Modal ---------------- */

const AuthModal = ({
  open,
  initialTab,
  onClose,
}: {
  open: boolean;
  initialTab: "login" | "signup";
  onClose: () => void;
}) => {
  const [tab, setTab] = useState<"login" | "signup">(initialTab);
  const { login, register } = useAuth();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (open) {
      setTab(initialTab);
      setError(null);
    }
  }, [open, initialTab]);

  useEffect(() => {
    const handler = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    if (open) document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [open, onClose]);

  if (!open) return null;

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const formData = new FormData(e.target as HTMLFormElement);
    const email = formData.get("email") as string;
    const password = formData.get("password") as string;

    try {
      if (tab === "login") {
        await login(email, password);
      } else {
        const fullName = formData.get("fullName") as string;
        const accountType = formData.get("accountType") as string;
        await register({ email, password, fullName, accountType });
      }
      onClose();
    } catch (err: any) {
      setError(err.message || "An error occurred");
    } finally {
      setLoading(false);
    }
  };

  const inputClass =
    "w-full rounded-lg border border-border bg-background/60 px-3 py-2 text-sm outline-none focus:border-primary focus:ring-1 focus:ring-primary";

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-background/80 p-4 backdrop-blur"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-md rounded-2xl border border-border bg-card p-6 shadow-glow"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          onClick={onClose}
          className="absolute right-4 top-4 text-muted-foreground hover:text-foreground"
          aria-label="Close"
        >
          <Icon name="close" className="h-5 w-5" />
        </button>

        <div className="mb-6">
          <h3 className="text-xl font-semibold">Welcome to CLUE BDI</h3>
          <p className="mt-1 text-sm text-muted-foreground">
            Access portfolio demos, dashboards & resources.
          </p>
        </div>

        <div className="mb-6 flex rounded-lg border border-border bg-secondary/40 p-1">
          {(["login", "signup"] as const).map((t) => (
            <button
              key={t}
              onClick={() => setTab(t)}
              className={`flex-1 rounded-md px-3 py-1.5 text-sm font-medium capitalize transition ${
                tab === t
                  ? "bg-primary-gradient text-primary-foreground"
                  : "text-muted-foreground hover:text-foreground"
              }`}
            >
              {t === "login" ? "Login" : "Sign Up"}
            </button>
          ))}
        </div>

        {error && (
          <div className="mb-4 rounded-lg bg-destructive/10 p-3 text-xs text-destructive">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          {tab === "signup" && (
            <div>
              <label className="mb-1 block text-xs font-medium text-muted-foreground">
                Full name
              </label>
              <input name="fullName" className={inputClass} placeholder="Jane Doe" required />
            </div>
          )}
          <div>
            <label className="mb-1 block text-xs font-medium text-muted-foreground">
              Email
            </label>
            <input
              name="email"
              type="email"
              className={inputClass}
              placeholder="you@company.com"
              required
            />
          </div>
          <div>
            <label className="mb-1 block text-xs font-medium text-muted-foreground">
              Password
            </label>
            <input
              name="password"
              type="password"
              className={inputClass}
              placeholder="••••••••"
              required
            />
          </div>
          {tab === "signup" && (
            <div>
              <label className="mb-1 block text-xs font-medium text-muted-foreground">
                Account type
              </label>
              <select name="accountType" className={inputClass} defaultValue={ACCOUNT_TYPES[0]}>
                {ACCOUNT_TYPES.map((a) => (
                  <option key={a} value={a} className="bg-card">
                    {a}
                  </option>
                ))}
              </select>
            </div>
          )}
          <Button type="submit" variant="primary" size="lg" className="w-full" onClick={() => {}}>
            {loading ? "Processing..." : tab === "login" ? "Sign in" : "Create account"}
          </Button>
        </form>

        <p className="mt-4 text-center text-[11px] leading-relaxed text-muted-foreground">
          Connected to CLUE BDI Portfolio Backend.
        </p>
      </div>
    </div>
  );
};

/* ---------------- Sections ---------------- */

const Header = ({
  onLogin,
  onSignup,
}: {
  onLogin: () => void;
  onSignup: () => void;
}) => {
  const [open, setOpen] = useState(false);
  const { user, logout } = useAuth();

  return (
    <header className="sticky top-0 z-40 border-b border-border/60 bg-background/80 backdrop-blur-xl">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
        <a href="#home" className="flex items-center gap-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary-gradient text-primary-foreground shadow-glow">
            <Icon name="shield" className="h-5 w-5" />
          </div>
          <div className="leading-tight">
            <div className="text-sm font-bold tracking-wide">CLUE BDI</div>
            <div className="text-[10px] uppercase tracking-wider text-muted-foreground">
              Business Data Intelligence
            </div>
          </div>
        </a>

        <nav className="hidden items-center gap-7 md:flex">
          {NAV_ITEMS.map((n) => (
            <a
              key={n.label}
              href={n.href}
              className="text-sm text-muted-foreground transition hover:text-foreground"
            >
              {n.label}
            </a>
          ))}
        </nav>

        <div className="hidden items-center gap-2 md:flex">
          {user ? (
            <>
              {user.accountType === "Staff" && (
                <Link to="/admin" className="mr-2 text-sm font-medium text-primary hover:underline">
                  Admin
                </Link>
              )}
              <span className="mr-2 text-sm font-medium text-muted-foreground">
                Hi, {user.fullName || user.email.split("@")[0]}
              </span>
              <Button variant="ghost" size="sm" onClick={logout}>
                Logout
              </Button>
            </>
          ) : (
            <>
              <Button variant="ghost" size="sm" onClick={onLogin}>
                Login
              </Button>
              <Button variant="secondary" size="sm" onClick={onSignup}>
                Sign Up
              </Button>
            </>
          )}
          <Button variant="primary" size="sm" onClick={() => window.open("https://drive.google.com/file/d/1FzG-VEj5Qf6VUJmI0relWZMpTl4dr7FO/view?usp=sharing", "_blank")}>
            <Icon name="download" className="h-4 w-4" />
            Download Resume
          </Button>
        </div>

        <button
          className="md:hidden text-foreground"
          onClick={() => setOpen((v) => !v)}
          aria-label="Menu"
        >
          <Icon name={open ? "close" : "menu"} className="h-6 w-6" />
        </button>
      </div>

      {open && (
        <div className="border-t border-border bg-background md:hidden">
          <div className="space-y-1 px-4 py-3">
            {NAV_ITEMS.map((n) => (
              <a
                key={n.label}
                href={n.href}
                onClick={() => setOpen(false)}
                className="block rounded-md px-3 py-2 text-sm text-muted-foreground hover:bg-secondary hover:text-foreground"
              >
                {n.label}
              </a>
            ))}
            <div className="flex flex-col gap-2 pt-3">
              {user ? (
                <Button variant="secondary" size="sm" onClick={logout}>
                  Logout
                </Button>
              ) : (
                <>
                  <Button variant="secondary" size="sm" onClick={onLogin}>
                    Login
                  </Button>
                  <Button variant="secondary" size="sm" onClick={onSignup}>
                    Sign Up
                  </Button>
                </>
              )}
              <Button variant="primary" size="sm" onClick={() => window.open("https://drive.google.com/file/d/1FzG-VEj5Qf6VUJmI0relWZMpTl4dr7FO/view?usp=sharing", "_blank")}>
                <Icon name="download" className="h-4 w-4" />
                Download Resume
              </Button>
            </div>
          </div>
        </div>
      )}
    </header>
  );
};

const Hero = ({ onCreateAccount }: { onCreateAccount: () => void }) => (
  <section id="home" className="relative overflow-hidden bg-hero-gradient">
    <div className="mx-auto grid max-w-7xl gap-12 px-4 py-20 sm:px-6 lg:grid-cols-2 lg:gap-8 lg:px-8 lg:py-28">
      <div>
        <span className="inline-flex items-center gap-2 rounded-full border border-primary/30 bg-primary/10 px-3 py-1 text-xs font-medium text-primary">
          <span className="h-1.5 w-1.5 rounded-full bg-primary" />
          Cloud · DevSecOps · Data Engineering Portfolio
        </span>
        <h1 className="mt-6 text-4xl font-bold tracking-tight sm:text-5xl lg:text-6xl">
          Build. Secure. <br />
          <span className="text-primary-gradient">Automate. Visualize.</span>
        </h1>
        <p className="mt-6 max-w-xl text-lg text-muted-foreground">
          A portfolio hub for cloud engineering projects, CI/CD security automation, blue/green
          deployment demos, and data intelligence dashboards built by CLUE BDI LLC.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <Button variant="primary" size="lg">
            View Projects
            <Icon name="arrow" />
          </Button>
          <Button variant="secondary" size="lg">
            <Icon name="play" className="h-4 w-4" />
            Explore Live Demos
          </Button>
          <Button variant="outline" size="lg" onClick={onCreateAccount}>
            Create Account
          </Button>
        </div>
        <div className="mt-8 flex flex-wrap gap-2">
          {SKILLS.map((s) => (
            <Pill key={s}>{s}</Pill>
          ))}
        </div>
      </div>

      <DashboardPreview />
    </div>
  </section>
);

const DashboardPreview = () => {
  const { data: posture, isLoading } = usePosture();

  return (
    <div className="relative">
      <div className="absolute -inset-4 rounded-3xl bg-primary/10 blur-3xl" />
      <div className="relative overflow-hidden rounded-2xl border border-border bg-card shadow-card">
        <div className="flex items-center gap-2 border-b border-border bg-secondary/40 px-4 py-3">
          <span className="h-3 w-3 rounded-full bg-destructive/70" />
          <span className="h-3 w-3 rounded-full bg-yellow-500/70" />
          <span className="h-3 w-3 rounded-full bg-emerald-500/70" />
          <div className="ml-3 flex-1 truncate rounded-md bg-background/60 px-3 py-1 text-xs text-muted-foreground">
            cluebdi.io / dashboard / security
          </div>
        </div>
        <div className="p-6">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-xs uppercase tracking-wider text-muted-foreground">
                Security posture
              </div>
              <div className="mt-1 text-2xl font-semibold">Improving</div>
            </div>
            <span className="rounded-full border border-emerald-500/30 bg-emerald-500/10 px-3 py-1 text-xs font-medium text-emerald-400">
              ▲ 24% this quarter
            </span>
          </div>
          <div className="mt-6 space-y-5">
            {isLoading ? (
              <div className="py-4 text-center text-sm text-muted-foreground">
                Loading posture data...
              </div>
            ) : (
              posture?.map((p) => (
                <div key={p.id}>
                  <div className="mb-1.5 flex items-center justify-between text-sm">
                    <span className="font-medium">{p.label}</span>
                    <span className="text-muted-foreground">
                      {p.note} — {p.value}%
                    </span>
                  </div>
                  <div className="h-2 overflow-hidden rounded-full bg-secondary">
                    <div
                      className="h-full rounded-full bg-primary-gradient"
                      style={{ width: `${p.value}%` }}
                    />
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

const Metrics = () => {
  const { data: metrics, isLoading } = useMetrics();

  return (
    <section className="border-y border-border bg-card/30">
      <div className="mx-auto grid max-w-7xl gap-8 px-4 py-12 sm:grid-cols-2 sm:px-6 lg:grid-cols-4 lg:px-8">
        {isLoading ? (
          <div className="col-span-full py-4 text-center text-sm text-muted-foreground">
            Loading metrics...
          </div>
        ) : (
          metrics?.map((m) => (
            <div key={m.id} className="text-center sm:text-left">
              <div className="text-2xl font-bold text-primary-gradient sm:text-3xl">{m.value}</div>
              <div className="mt-1 text-sm text-muted-foreground">{m.label}</div>
            </div>
          ))
        )}
      </div>
    </section>
  );
};

const Projects = () => {
  const [active, setActive] = useState<Category | "All">("All");
  const { data: projects, isLoading } = useProjects();

  const filtered = useMemo(
    () =>
      active === "All" ? projects : projects?.filter((p: Project) => p.category === active),
    [active, projects],
  );

  return (
    <section id="projects" className="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <SectionHeading
        eyebrow="Projects"
        title="Portfolio projects recruiters can scan quickly"
        subtitle="Each project shows real engineering depth across cloud, security automation, and data pipelines — with demo links and dashboards."
      />
      <div className="mb-8 flex flex-wrap gap-2">
        {CATEGORIES.map((c) => (
          <button
            key={c}
            onClick={() => setActive(c)}
            className={`rounded-full border px-4 py-1.5 text-sm font-medium transition ${
              active === c
                ? "border-primary bg-primary/10 text-primary"
                : "border-border bg-secondary/40 text-muted-foreground hover:text-foreground"
            }`}
          >
            {c}
          </button>
        ))}
      </div>
      <div className="grid gap-6 md:grid-cols-2">
        {isLoading ? (
          <div className="col-span-full py-20 text-center text-sm text-muted-foreground">
            Loading projects...
          </div>
        ) : (
          filtered?.map((p: Project) => <ProjectCard key={p.id} project={p} />)
        )}
      </div>
    </section>
  );
};

const Demos = () => (
  <section id="demos" className="border-y border-border bg-card/30">
    <div className="mx-auto grid max-w-7xl gap-12 px-4 py-20 sm:px-6 lg:grid-cols-2 lg:px-8">
      <div>
        <SectionHeading
          eyebrow="Live Demo"
          title="Blue/Green deployment showcase"
          subtitle="A safe, fully reproducible scenario: a vulnerable blue version is deployed, scanned in CI/CD, then replaced with a patched green version. The dashboard shows measurable vulnerability reduction."
        />
        <Button variant="primary" size="lg" onClick={() => window.open("http://104.43.135.132", "_blank")}>
          <Icon name="play" />
          Launch the demo
        </Button>
      </div>
      <div className="rounded-2xl border border-border bg-card p-8 shadow-card">
        <ul className="space-y-4">
          {DEMO_CHECKLIST.map((item) => (
            <li key={item} className="flex items-start gap-3">
              <span className="mt-0.5 flex h-6 w-6 flex-none items-center justify-center rounded-full bg-primary/15 text-primary">
                <Icon name="check" className="h-4 w-4" />
              </span>
              <span className="text-sm text-foreground">{item}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  </section>
);

const Architecture = () => (
  <section id="architecture" className="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
    <SectionHeading
      eyebrow="Architecture"
      title="From commit to dashboard"
      subtitle="Every step is automated, scanned, and observable — so security and analytics flow naturally through the pipeline."
      center
    />
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {ARCH_STEPS.map((s, i) => (
        <div
          key={s.title}
          className="group relative rounded-2xl border border-border bg-card/60 p-6 transition hover:border-primary/40"
        >
          <div className="mb-3 flex items-center gap-3">
            <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary/10 text-sm font-semibold text-primary">
              {String(i + 1).padStart(2, "0")}
            </span>
            <h3 className="text-lg font-semibold">{s.title}</h3>
          </div>
          <p className="text-sm text-muted-foreground">{s.text}</p>
        </div>
      ))}
    </div>
  </section>
);

const TechTable = () => (
  <section className="border-y border-border bg-card/30">
    <div className="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <SectionHeading
        eyebrow="Reference"
        title="Use clean tables for technical depth"
        subtitle="A compact map of how this portfolio is structured — designed for fast skimming by recruiters and engineering leads."
      />
      <div className="overflow-hidden rounded-2xl border border-border bg-card">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="bg-secondary/40 text-xs uppercase tracking-wider text-muted-foreground">
              <tr>
                <th className="px-6 py-4">Component</th>
                <th className="px-6 py-4">Recommended Content</th>
                <th className="px-6 py-4">Purpose</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border">
              {TABLE_ROWS.map((row) => (
                <tr key={row[0]} className="hover:bg-secondary/30">
                  <td className="px-6 py-4 font-medium text-foreground">{row[0]}</td>
                  <td className="px-6 py-4 text-muted-foreground">{row[1]}</td>
                  <td className="px-6 py-4 text-muted-foreground">{row[2]}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
);

const Contact = () => (
  <section id="contact" className="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
    <div className="relative overflow-hidden rounded-3xl border border-border bg-card p-10 text-center shadow-card sm:p-16">
      <div className="absolute inset-0 bg-hero-gradient opacity-60" />
      <div className="relative">
        <SectionHeading
          eyebrow="Contact"
          title="Let's connect"
          subtitle="Add LinkedIn, GitLab/GitHub, resume, and email here so visitors can move from interest to action quickly."
          center
        />
        <div className="flex flex-wrap justify-center gap-3">
          <Button 
            variant="primary" 
            size="lg"
            onClick={() => window.open("https://www.linkedin.com/in/mjhasan1", "_blank")}
          >
            <Icon name="linkedin" />
            LinkedIn
          </Button>
          <Button 
            variant="secondary" 
            size="lg"
            onClick={() => window.open("https://github.com/CLUE-BDI", "_blank")}
          >
            <Icon name="github" />
            GitHub
          </Button>
          <Button 
            variant="secondary" 
            size="lg"
            onClick={() => window.open("https://drive.google.com/file/d/1FzG-VEj5Qf6VUJmI0relWZMpTl4dr7FO/view?usp=sharing", "_blank")}
          >
            <Icon name="download" />
            Resume
          </Button>
          <Button 
            variant="outline" 
            size="lg"
            onClick={() => window.location.href = "mailto:jakirul@gmail.com"}
          >
            <Icon name="mail" />
            Email
          </Button>
        </div>
      </div>
    </div>
  </section>
);

const Footer = () => (
  <footer className="border-t border-border py-8">
    <div className="mx-auto max-w-7xl px-4 text-center text-sm text-muted-foreground sm:px-6 lg:px-8">
      © 2026 CLUE BDI LLC · Cloud, DevSecOps & Data Intelligence Portfolio
    </div>
  </footer>
);

/* ---------------- Root ---------------- */

export default function Portfolio() {
  const [authOpen, setAuthOpen] = useState(false);
  const [authTab, setAuthTab] = useState<"login" | "signup">("login");

  const open = (tab: "login" | "signup") => {
    setAuthTab(tab);
    setAuthOpen(true);
  };

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header onLogin={() => open("login")} onSignup={() => open("signup")} />
      <main>
        <Hero onCreateAccount={() => open("signup")} />
        <Metrics />
        <Projects />
        <Demos />
        <Architecture />
        <TechTable />
        <Contact />
      </main>
      <Footer />
      <AuthModal open={authOpen} initialTab={authTab} onClose={() => setAuthOpen(false)} />
    </div>
  );
}