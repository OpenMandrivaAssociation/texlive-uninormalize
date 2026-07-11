%global tl_name uninormalize
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Unicode normalization support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/uninormalize
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uninormalize.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uninormalize.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides Unicode normalization (useful for composed
characters) for LuaLaTeX.

