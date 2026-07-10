%global tl_name docsurvey
%global tl_revision 70729

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A survey of LaTeX documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/docsurvey
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docsurvey.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docsurvey.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A survey of programming-related documentation for LaTeX. Included are
references to printed and electronic books and manuals, symbol lists,
FAQs, the LaTeX source code, CTAN and distributions, programming-related
packages, users groups and online communities, and information on
creating packages and documentation.

